<script lang="ts">
</script>


<div id="thebutton">
    <button class="bg-orange-500 p-5 ml-4 my-4 rounded w-64 h-20 text-2xl"
    onclick={async () => {
        let res = await fetch("/api/scan", {method: "POST"})
        if (res.ok) {
            window.location.href = "/realtime"
        }
    }}>Scan</button>
</div>
