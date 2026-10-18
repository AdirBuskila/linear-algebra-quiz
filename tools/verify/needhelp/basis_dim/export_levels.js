// prints the basis_dim level files as JSON (stub COURSE_LEVEL)
const fs = require("fs"), path = require("path"), vm = require("vm");
const dir = path.join(__dirname, "..", "..", "..", "..", "courses", "basis_dim");
const out = [];
for (const f of fs.readdirSync(dir).filter(f => /^C\d+\.js$/.test(f)).sort()) {
  vm.runInNewContext(fs.readFileSync(path.join(dir, f), "utf8"), { COURSE_LEVEL: (id, L) => out.push(L) });
}
process.stdout.write(JSON.stringify(out));
