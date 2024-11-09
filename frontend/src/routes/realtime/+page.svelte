<script lang="ts">
	import Scanview from "$lib/components/Scanview.svelte";
	import { Device, Scan, Vulnerability } from "$lib/scan";
	import { onMount } from "svelte";
    import {humanScanType} from "$lib/humanScanType"

    let status: { 
        agent: string, 
        type: string, 
        host: string, 
        cve: {id: string, severity: string}[], 
        cpe: string 
    }

    let registeredHosts: string[] = []

    async function fetchScanStatus() {
        const response = await fetch('/api/scan');
        if (response.ok) {
            status = await response.json();
            if (status.agent == "final") {
                lastStatus = "done"
                return
            }
            lastStatus = status.type

            if (status.agent == "scanner" && status.type == "host up") {
                if (registeredHosts.includes(status.host)) return
                registeredHosts.push(status.host)
                devices.push(new Device(status.host, status.host, []))
            }
            console.info(status.agent)

            if (status.agent == "cve-assign") {
                let deviceID = devices.findIndex((dev) => dev.ip == status.host)
                console.log(deviceID)
                if (deviceID == -1) return;
                for (let cve of status.cve) {
                    devices[deviceID].vulnerabilities.push(new Vulnerability(cve.id, cve.severity))
                    devices[deviceID] = devices[deviceID]
                }
                console.log(devices)
            }
            
            console.log(status)

        } else {
            if (lastStatus != "done") {
                lastStatus = "idle"
            }
            // window.location.href = "/history"
        }
    }

    onMount(() => {
        fetchScanStatus();
        let intervalId = setInterval(fetchScanStatus, 100); 

        return () => {
            clearInterval(intervalId);
        };
    });

    let networkName = $state("Realtime scan")
    let lastStatus = $state("")
    let humanStatus = $derived(humanScanType[lastStatus])
    let date = $state(new Date())
    let devices: Device[] = $state([])
</script>

<Scanview networkName={networkName} description={humanStatus} date={date} devices={devices}></Scanview>


