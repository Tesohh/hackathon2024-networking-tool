<script lang="ts">
	import { page } from '$app/stores';
	import '../app.css';
	let { children } = $props();
</script>

<div class="fixed top-0 left-0 h-full w-64 flex flex-col" id="sidebar">

    <div class="py-5 px-10 text-2xl" id="sidebarlinks">
        <p>VMaps</p><br>
        <a href="/" class={$page.url.pathname == "/" ? "text-orange-500 font-bold" : ""}>Home</a><br>
        <a href="/history" class={$page.url.pathname == "/history" ? "text-orange-500 font-bold" : ""}>Scan History</a>
        <a href="/example" class={$page.url.pathname == "/example" ? "text-orange-500 font-bold" : ""}>Example</a>
    </div>

    <div class="grow"></div>

    <div id="thebutton">
        <button class="bg-orange-500 p-5 ml-4 my-4 rounded w-64 h-20 text-2xl">Scan</button>
    </div>
</div>

<div class="ml-64 mt-10">
    {@render children()}
</div>

