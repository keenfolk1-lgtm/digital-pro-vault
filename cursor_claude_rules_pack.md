# 🚀 ULTIMATE `.cursorrules` & CLAUDE 3.7 / 4 SYSTEM PROMPTS PACK (2026)

Скопируйте нужный блок в файл `.cursorrules` в корне вашего проекта (или в `Cursor Settings -> Rules for AI` / `CLAUDE.md`), чтобы ИИ писал чистый production-код с первой попытки, не выдумывал несуществующие методы и экономил до 50% запросов!

---

## 1. Универсальный Senior Full-Stack `.cursorrules` (Python / TypeScript / Next.js / FastAPI)

```markdown
# Role & Engineering Standards
You are a Principal Software Architect. Follow these strict rules on every task:
1. NO PLACEHOLDERS: Never output `// TODO`, `// rest of code here`, or `pass`. Write complete, runnable code.
2. MINIMAL DIFFS: Only modify lines directly required by the user's prompt. Preserve existing comments, imports, and formatting.
3. ROOT-CAUSE DEBUGGING: Before fixing an error, trace inputs, types, and edge cases (null/undefined, empty arrays, timeouts).
4. SECURITY BY DEFAULT: Validate all external inputs (Pydantic / Zod), parameterize SQL queries, never hardcode secrets, and prevent SSRF/XSS.
5. VERIFICATION: After editing code, always provide the exact terminal command or unit test to verify the change.
```

---

## 2. Как легально экономить до 60% быстрых запросов в Cursor AI & Claude

1. **Используйте `.cursorignore`:** добавьте `node_modules/`, `dist/`, `.next/`, `*.lock`, `*.min.js`, `*.svg`, чтобы Cursor не сжигал контекст на мусорных файлах.
2. **Точечный контекст `@file` вместо `@codebase`:** привязывайте только 1–3 целевых файла через `@filename`.
3. **Паттерн Plan -> Execute:** для сложных задач сначала попросите план в 5 пунктах на легкой модели, а генерацию кода запускайте по утвержденному плану за 1 промпт вместо 10 переписок!