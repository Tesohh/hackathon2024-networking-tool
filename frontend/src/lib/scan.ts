export class Device {
    public name: string;
    public vulnerabilities: Vulnerability[];

    constructor(name: string, vulnerabilities: Vulnerability[]) {
        this.name = name;
        this.vulnerabilities = vulnerabilities;
    }
}

export function lowVulns(vulnerabilities: Vulnerability[]): Vulnerability[] {
    return vulnerabilities.filter((v) => v.severity == "LOW");
}
export function mediumVulns(vulnerabilities: Vulnerability[]): Vulnerability[] {
    return vulnerabilities.filter((v) => v.severity == "MEDIUM");
}
export function highVulns(vulnerabilities: Vulnerability[]): Vulnerability[] {
    return vulnerabilities.filter((v) => v.severity == "HIGH");
}

export class Vulnerability {
    public name: string;
    public severity: string;

    constructor(name: string, severity: string) {
        this.name = name;
        this.severity = severity;
    }

    public icon(): string {
        switch (this.severity) {
            case "LOW":
                return "🔵";
            case "MEDIUM":
                return "⚠️";
            case "HIGH":
                return "🛑";
            default:
                return "👽";
        }
    }
}

export class Scan {
    public networkName: string;
    public date: Date;
    public devices: Device[];

    constructor(networkName: string, date: Date, devices: Device[]) {
        this.networkName = networkName;
        this.date = date;
        this.devices = devices;
    }
}
