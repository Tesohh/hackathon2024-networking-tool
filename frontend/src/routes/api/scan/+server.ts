import { spawn } from "child_process";
export async function POST(event: any) {
	if (isScanning) {
		return new Response("scan already running", { status: 500 });
	}

	startScan();
	return new Response();
} // starts (if possible) the scan

export async function PATCH(event: any) {
	return new Response(isScanning ? "true" : "false");
}

export async function GET(event: any) {
	if (!isScanning) {
		return new Response("not scanning", { status: 500 });
	}

	return new Response(latestUpdate);
} // returns last status

let isScanning = false;
let latestUpdate = "";
async function startScan() {
	isScanning = true;
	// TODO: get from ENV
	console.log("started scan.");
	let scanner = spawn("python3", ["../scanner/main.py", "en0"]);
	scanner.stdout.on("data", (data: any) => {
		console.log(data.toString());
		latestUpdate = data.toString();
	});
	scanner.stderr.on("data", (data: any) => {
		console.error(`stderr: ${data}`);
	});

	scanner.on("close", (code: any) => {
		console.log(`child process exited with code ${code}`);
		isScanning = false;
	});
}
