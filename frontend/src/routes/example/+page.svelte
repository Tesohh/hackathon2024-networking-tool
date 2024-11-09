<script lang="ts">
    import Scanview from "$lib/components/Scanview.svelte";
	import { Device, Scan, Vulnerability } from "$lib/scan";

    let scan = new Scan("NETWORK 1", new Date(), [
        new Device("Herris PC", [new Vulnerability("CVE-6969", "HIGH"), new Vulnerability("CVE-1234", "MEDIUM")]),
        new Device("Autoherrimilian", [new Vulnerability("CVE-6969", "MEDIUM")]),
        new Device("Herissa", [])
    ])
    
    let networkName = $state(scan.networkName)
    let date = $state(scan.date)
    let devices = $state(scan.devices)

</script>

<Scanview networkName={networkName} date={date} devices={devices}></Scanview>
<button onclick={() => { networkName = "NETWROK 2" }}>Change network</button>
