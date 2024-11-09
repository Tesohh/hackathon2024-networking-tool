import { spawn } from "child_process";
export async function POST(event: any) {
	if (isScanning) {
		return new Response("scan already running", { status: 500 });
	}

	startScan();
	return new Response();
} // starts (if possible) the scan
export async function GET(event: any) {} // returns last status

let isScanning = false;
let latestUpdate = "";
async function startScan() {
	isScanning = true;
	// TODO: get from ENV
	console.log("The Proof");
	let scanner = spawn("python3", ["../scanner/main.py", "en0"]);
	console.log(spawn);
	console.log(scanner);
	scanner.stdout.on("data", (data) => {
		console.log(`stdout: ${data}`);
	});
	scanner.stderr.on("data", (data) => {
		console.error(`stderr: ${data}`);
	});

	scanner.on("close", (code) => {
		console.log(`child process exited with code ${code}`);
	});

	// isScanning = false;
}
