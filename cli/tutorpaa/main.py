#!/usr/bin/env python3
"""TutorPAA CLI inicial sin dependencias externas."""

from __future__ import annotations

import argparse
import json
import random
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONTENT_ROOT = ROOT / "content" / "paa"
SESSIONS_ROOT = ROOT / "sessions" / "students"
ERROR_TYPES = {"concept", "calculation", "reading", "strategy", "time", "careless", "unknown", "none"}


def load_questions(section: str | None = None) -> list[dict]:
    questions: list[dict] = []
    roots = [CONTENT_ROOT / section] if section else [CONTENT_ROOT / "math", CONTENT_ROOT / "verbal"]
    for root in roots:
        if not root.exists():
            continue
        for path in sorted(root.glob("*.jsonl")):
            with path.open("r", encoding="utf-8") as handle:
                for line_number, line in enumerate(handle, start=1):
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        item = json.loads(line)
                    except json.JSONDecodeError as exc:
                        raise SystemExit(f"JSON invalido en {path}:{line_number}: {exc}") from exc
                    if item.get("status") == "curated":
                        questions.append(item)
    return questions


def ensure_student(student: str) -> Path:
    student_dir = SESSIONS_ROOT / student
    student_dir.mkdir(parents=True, exist_ok=True)
    profile = student_dir / "profile.json"
    attempts = student_dir / "attempts.jsonl"
    if not profile.exists():
        profile.write_text(
            json.dumps(
                {
                    "student_id": student,
                    "name": student,
                    "goal_score": None,
                    "target_program": "USFQ",
                    "notes": "Perfil creado por CLI.",
                    "created_at": datetime.now(timezone.utc).date().isoformat(),
                },
                indent=2,
                ensure_ascii=True,
            )
            + "\n",
            encoding="utf-8",
        )
    if not attempts.exists():
        attempts.write_text("", encoding="utf-8")
    return student_dir


def append_attempt(student: str, record: dict) -> None:
    student_dir = ensure_student(student)
    attempts = student_dir / "attempts.jsonl"
    with attempts.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=True) + "\n")


def find_question(question_id: str) -> dict:
    for question in load_questions():
        if question.get("id") == question_id:
            return question
    raise SystemExit(f"No existe question_id: {question_id}")


def run_practice(args: argparse.Namespace) -> None:
    ensure_student(args.student)
    questions = load_questions(args.section)
    if args.topic:
        questions = [q for q in questions if q.get("topic") == args.topic]
    if not questions:
        raise SystemExit("No hay preguntas curated para ese filtro.")

    selected = random.sample(questions, k=min(args.count, len(questions)))
    correct = 0

    print(f"TutorPAA practica: student={args.student} section={args.section or 'all'} count={len(selected)}")
    print("Responde con el texto exacto de una opcion o su numero.\n")

    for index, question in enumerate(selected, start=1):
        choices = question["choices"]
        print(f"{index}. [{question['section']} / {question['topic']}] {question['question']}")
        for choice_index, choice in enumerate(choices, start=1):
            print(f"  {choice_index}. {choice}")
        raw = input("Tu respuesta: ").strip()
        answer = normalize_answer(raw, choices)
        is_correct = answer == question["answer"]
        correct += 1 if is_correct else 0

        print("Correcto." if is_correct else f"Incorrecto. Respuesta: {question['answer']}")
        print(f"Explicacion: {question['explanation']}\n")

        append_attempt(
            args.student,
            {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "question_id": question["id"],
                "section": question["section"],
                "topic": question["topic"],
                "skills": question.get("skills", []),
                "answer": answer,
                "correct_answer": question["answer"],
                "is_correct": is_correct,
                "student_reasoning": "",
                "error_type": "none" if is_correct else "unknown",
                "confidence": None,
                "source": "cli-practice",
            },
        )

    print(f"Resultado: {correct}/{len(selected)}")


def normalize_answer(raw: str, choices: list[str]) -> str:
    cleaned = raw.strip()
    if cleaned.isdigit():
        idx = int(cleaned) - 1
        if 0 <= idx < len(choices):
            return choices[idx]
    if len(cleaned) == 1 and cleaned.upper().isalpha():
        idx = ord(cleaned.upper()) - ord("A")
        if 0 <= idx < len(choices):
            return choices[idx]
    return cleaned


def format_question(question: dict, number: int = 1) -> str:
    labels = ["A", "B", "C", "D", "E"]
    lines = [
        f"Pregunta {number} [{question['section']} / {question['topic']} / dificultad {question['difficulty']}]:",
        question["question"],
        "",
        "Opciones:",
    ]
    for idx, choice in enumerate(question["choices"]):
        label = labels[idx] if idx < len(labels) else str(idx + 1)
        lines.append(f"{label}. {choice}")
    lines.extend(["", "Responde con A, B, C o D, tu razonamiento y confianza del 1 al 5."])
    return "\n".join(lines)


def run_pick(args: argparse.Namespace) -> None:
    questions = load_questions(args.section)
    if args.topic:
        questions = [q for q in questions if q.get("topic") == args.topic]
    if args.skill:
        questions = [q for q in questions if args.skill in q.get("skills", [])]
    if not questions:
        raise SystemExit("No hay preguntas curated para ese filtro.")

    if args.random:
        selected = random.sample(questions, k=min(args.count, len(questions)))
    else:
        selected = questions[: args.count]

    for index, question in enumerate(selected, start=1):
        if args.format == "text":
            print(format_question(question, index))
            if index < len(selected):
                print("\n---\n")
        else:
            print(json.dumps(question, ensure_ascii=False))


def run_record(args: argparse.Namespace) -> None:
    question = find_question(args.question_id)
    answer = normalize_answer(args.answer, question["choices"])
    is_correct = answer == question["answer"]
    error_type = args.error_type
    if error_type not in ERROR_TYPES:
        raise SystemExit(f"error_type invalido: {error_type}")
    if is_correct and error_type == "unknown":
        error_type = "none"

    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "question_id": question["id"],
        "section": question["section"],
        "topic": question["topic"],
        "skills": question.get("skills", []),
        "answer": answer,
        "correct_answer": question["answer"],
        "is_correct": is_correct,
        "student_reasoning": args.reasoning or "",
        "error_type": error_type,
        "confidence": args.confidence,
        "source": "agent-session",
    }
    append_attempt(args.student, record)
    print(json.dumps(record, ensure_ascii=False, indent=2))


def run_session_prompt(args: argparse.Namespace) -> None:
    student = args.student
    ensure_student(student)
    prompt = f"""Lee AGENTS.md, docs/paa-model.md, docs/official-sources.md y prompts/agents/tutor.md.
Actua como tutor PAA agent-first para el estudiante `{student}`.

Modo de trabajo:
- Conversa conmigo como chat de practica, no como clase generica.
- No te detengas por falta de contenido; si el banco curado es pequeno, dilo en una frase y empieza.
- No me preguntes si quiero comenzar; empieza con la primera pregunta.
- Si pregunto que recomiendas, recomienda brevemente y empieza con una pregunta en el mismo mensaje.
- Haz una pregunta a la vez usando contenido curated de content/paa/.
- Muestra siempre todas las opciones antes de pedirme A/B/C/D.
- Para presentar preguntas, puedes usar: python3 cli/tutorpaa/main.py pick --format text.
- No reveles la respuesta hasta que intente resolver.
- Pideme opcion, razonamiento y confianza del 1 al 5.
- Corrige, explica y clasifica el error.
- Registra cada intento con:
  python3 cli/tutorpaa/main.py record --student {student} --question-id <id> --answer "<respuesta>" --reasoning "<razonamiento>" --confidence <1-5> --error-type <tipo>
- Cada 5 preguntas, ejecuta:
  python3 cli/tutorpaa/main.py report --student {student}

Empieza ahora con la primera pregunta. No hagas inventario del repositorio salvo una nota breve si es necesario, y no cierres preguntando si quiero iniciar."""
    print(prompt)


def run_report(args: argparse.Namespace) -> None:
    student_dir = ensure_student(args.student)
    attempts_path = student_dir / "attempts.jsonl"
    records = []
    with attempts_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    profile = json.loads((student_dir / "profile.json").read_text(encoding="utf-8"))
    print(f"Reporte TutorPAA: {profile.get('name', args.student)}")
    print(f"Intentos registrados: {len(records)}")
    if not records:
        print("Aun no hay practica registrada.")
        return

    correct = sum(1 for record in records if record["is_correct"])
    print(f"Precision total: {correct}/{len(records)} ({correct / len(records):.0%})")

    by_section: dict[str, list[dict]] = defaultdict(list)
    by_topic: dict[str, list[dict]] = defaultdict(list)
    missed_skills: Counter[str] = Counter()
    error_types: Counter[str] = Counter()
    for record in records:
        by_section[record["section"]].append(record)
        by_topic[record["topic"]].append(record)
        if not record["is_correct"]:
            missed_skills.update(record.get("skills", []))
            error_types.update([record.get("error_type", "unknown")])

    print("\nPor seccion:")
    for section, items in sorted(by_section.items()):
        section_correct = sum(1 for item in items if item["is_correct"])
        print(f"- {section}: {section_correct}/{len(items)} ({section_correct / len(items):.0%})")

    print("\nPor tema:")
    for topic, items in sorted(by_topic.items()):
        topic_correct = sum(1 for item in items if item["is_correct"])
        print(f"- {topic}: {topic_correct}/{len(items)} ({topic_correct / len(items):.0%})")

    if missed_skills:
        print("\nHabilidades a reforzar:")
        for skill, count in missed_skills.most_common(5):
            print(f"- {skill}: {count} error(es)")

    if error_types:
        print("\nTipos de error:")
        for error_type, count in error_types.most_common():
            print(f"- {error_type}: {count}")


def run_list(args: argparse.Namespace) -> None:
    questions = load_questions(args.section)
    topics = Counter(q["topic"] for q in questions)
    print(f"Preguntas curated: {len(questions)}")
    for topic, count in sorted(topics.items()):
        print(f"- {topic}: {count}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="TutorPAA CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    practice = subparsers.add_parser("practice", help="Practica preguntas curated.")
    practice.add_argument("--student", default="sample")
    practice.add_argument("--section", choices=["math", "verbal"], default=None)
    practice.add_argument("--topic", default=None)
    practice.add_argument("--count", type=int, default=5)
    practice.set_defaults(func=run_practice)

    report = subparsers.add_parser("report", help="Muestra progreso local.")
    report.add_argument("--student", default="sample")
    report.set_defaults(func=run_report)

    list_cmd = subparsers.add_parser("list", help="Lista contenido disponible.")
    list_cmd.add_argument("--section", choices=["math", "verbal"], default=None)
    list_cmd.set_defaults(func=run_list)

    pick = subparsers.add_parser("pick", help="Entrega preguntas JSON para que las use un agente.")
    pick.add_argument("--section", choices=["math", "verbal"], default=None)
    pick.add_argument("--topic", default=None)
    pick.add_argument("--skill", default=None)
    pick.add_argument("--count", type=int, default=1)
    pick.add_argument("--random", action="store_true")
    pick.add_argument("--format", choices=["json", "text"], default="json")
    pick.set_defaults(func=run_pick)

    record = subparsers.add_parser("record", help="Registra un intento corregido por agente.")
    record.add_argument("--student", default="sample")
    record.add_argument("--question-id", required=True)
    record.add_argument("--answer", required=True)
    record.add_argument("--reasoning", default="")
    record.add_argument("--confidence", type=int, choices=[1, 2, 3, 4, 5], default=None)
    record.add_argument("--error-type", default="unknown", choices=sorted(ERROR_TYPES))
    record.set_defaults(func=run_record)

    session_prompt = subparsers.add_parser("session-prompt", help="Imprime un prompt listo para iniciar con un agente AI.")
    session_prompt.add_argument("--student", default="sample")
    session_prompt.set_defaults(func=run_session_prompt)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
