<script lang="ts">
    let hidden = $state(false)
</script>

<!--save the opened item in the Scanview-->

<button onclick={() => hidden = !hidden}>
    <a></a>class={hidden ? "hidden" : ""} 
</button>
