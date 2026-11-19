// Entry program for the make.fun bounty "Post a GTA 6 meme on X"
// (competition slug: gta6-meme-x-01), written in the same agent session
// that created this repository and its meme.
//
// The job here is deliberately tiny. The entry itself is a public post on
// X: its first picture is the meme and its text carries the make.fun link
// and the entrant's play code. This program only has to hand the grader
// the post's address, which lives in POST.json at the repository root,
// by copying that file into the output directory byte for byte.
//
// When it runs outside the grader, MAKEFUN_BOT_DIR stands in for the
// repository mount and MAKEFUN_OUTPUT_DIR for the output mount:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
// On success it prints nothing.

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const botDir = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(outputDir, { recursive: true });

// Fail early with a clear message when POST.json is missing or is not a
// JSON object carrying a string "url". The file itself is still copied
// raw below, never re-serialised, so the output stays byte for byte
// identical to the repository's POST.json on every run.
let post: unknown;
try {
  post = JSON.parse(readFileSync(join(botDir, 'POST.json'), 'utf8'));
} catch (err) {
  console.error(`POST.json could not be read from ${botDir}: ${(err as Error).message}`);
  process.exit(1);
}
if (typeof post !== 'object' || post === null || typeof (post as { url?: unknown }).url !== 'string') {
  console.error('POST.json must be a JSON object with a string "url" naming the X post');
  process.exit(1);
}

try {
  copyFileSync(join(botDir, 'POST.json'), join(outputDir, 'POST.json'));
} catch (err) {
  console.error(`could not copy POST.json from ${botDir}: ${(err as Error).message}`);
  process.exit(1);
}
