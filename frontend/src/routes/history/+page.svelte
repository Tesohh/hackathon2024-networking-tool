<script lang="ts">
	import { page } from "$app/stores";
	import { onMount } from "svelte";

    const url = $page.url;
    let possibleDate = url.searchParams.get("date");
    let date = possibleDate != null ? new Date(possibleDate) : new Date();
</script>

{#if possibleDate == null}
    <span class="text-4xl font-bold">Latest Scan</span> 
{:else}
    <span class="text-4xl font-bold">{date.toDateString()} scan</span>
{/if}

<!-- TODO: -->
