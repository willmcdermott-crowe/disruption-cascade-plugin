#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const os = require('os');

const PLUGIN_NAME = 'Disruption Cascade';
const DIST_DIR = path.join(__dirname, '..', 'dist', 'claude-code');

function copyRecursive(src, dest) {
  if (!fs.existsSync(src)) return;
  const stat = fs.statSync(src);
  if (stat.isDirectory()) {
    if (!fs.existsSync(dest)) fs.mkdirSync(dest, { recursive: true });
    for (const item of fs.readdirSync(src)) {
      copyRecursive(path.join(src, item), path.join(dest, item));
    }
  } else {
    const destDir = path.dirname(dest);
    if (!fs.existsSync(destDir)) fs.mkdirSync(destDir, { recursive: true });
    fs.copyFileSync(src, dest);
  }
}

const args = process.argv.slice(2);
const isGlobal = args.includes('--global') || args.includes('-g');

console.log('');
console.log('  Disruption Cascade');
console.log('  ──────────────────────────────────────────────');
console.log('');

if (isGlobal) {
  const claudeDir = path.join(os.homedir(), '.claude');
  copyRecursive(path.join(DIST_DIR, '.claude'), claudeDir);

  console.log('  ✓ Installed globally to ~/.claude/');
  console.log('');
  console.log('  /run is now available in all Claude Code projects.');
  console.log('  Run outputs save into prototype/ in each project.');
  console.log('');
  console.log('  Note: Global install includes commands and rules only.');
  console.log('  For move templates, use project install: npx disruption-cascade-plugin');
  console.log('');
} else {
  const targetDir = process.cwd();

  for (const item of fs.readdirSync(DIST_DIR)) {
    copyRecursive(path.join(DIST_DIR, item), path.join(targetDir, item));
  }

  console.log('  ✓ Installed to ' + targetDir);
  console.log('');
  console.log('  Open Claude Code in this folder and type:');
  console.log('');
  console.log('    /run CFO Manufacturing "Mid-Market ($100M–$1B revenue)"');
  console.log('');
  console.log('  Run outputs save to prototype/ in this folder.');
  console.log('');
}
