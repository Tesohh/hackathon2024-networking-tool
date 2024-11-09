<script lang="ts">
    import Scanview from "$lib/components/Scanview.svelte";
	import { Device, Scan, Vulnerability } from "$lib/scan";

    let scan = new Scan("NETWORK 1", new Date(), [
        new Device("Macbook air", [new Vulnerability("CVE-1999-0199", "HIGH"), new Vulnerability("CVE-2023-44090", "MEDIUM")]),
        new Device("Sony Vaio", [new Vulnerability("CVE-2008-10003", "LOW"), new Vulnerability("CVE-2008-7291", "HIGH")]),
        new Device("Samsung Smart Display", []),
        new Device("Sennheiser Smart Speaker", [new Vulnerability("CVE-2019-8920", "MEDIUM")])
    ])
    
    let networkName = $state(scan.networkName)
    let date = $state(scan.date)
    let devices = $state(scan.devices)

</script>

<Scanview networkName={networkName} date={date} devices={devices}></Scanview>
