<script lang="ts">
    import {Device, Scan, lowVulns, mediumVulns, highVulns} from "$lib/scan";
    import ToggleableListItem from "./ToggleableListItem.svelte"; 
    let {networkName, date, devices}: Scan = $props()
    let selectedDevice: Device | undefined = $state();
</script>

<p class="text-4xl font-bold">{networkName}</p>
<div class="flex flex-col space-y-3">
{#each devices as device}
    <button class="bg-[#343434] border-gray-700 border-solid border-2 rounded p-3 w-64 flex flex-row"
            onclick={() => {
                if (selectedDevice == device) selectedDevice = undefined
                else selectedDevice = device
            }}>
            <span>{device.name}</span>
            <div class="grow"></div>
            <div class="">
                {#if lowVulns(device.vulnerabilities).length > 0}
                    <span>🔵 {lowVulns(device.vulnerabilities).length}</span>
                {/if}
                {#if mediumVulns(device.vulnerabilities).length > 0}
                    <span>⚠️ {mediumVulns(device.vulnerabilities).length}</span>
                {/if}
                {#if highVulns(device.vulnerabilities).length > 0}
                    <span>🛑 {highVulns(device.vulnerabilities).length}</span>
                {/if}
            </div>
        </button>
    {#if device == selectedDevice}
        {#if device.vulnerabilities.length == 0}
            <p>no vulnerabilities :)</p>
        {:else}
            <div class="space-y-0">
            {#each device.vulnerabilities as vuln}
                <div class="bg-gray-500 w-56 px-4 ml-8">
                    <p>{vuln.name}</p>
                </div>
            {/each}
            </div>
        {/if}
    {/if}
{/each}
</div>

