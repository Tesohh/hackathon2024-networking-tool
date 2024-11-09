<script>
	import data from '$lib/example.json'
	let show = false;
	let dataMap = new Map(Object.entries(data));
	let color = "green"
</script>

<link href='https://fonts.googleapis.com/css?family=Afacad' rel='stylesheet'>

	<div class="flex flex-wrap"  id="header">
		<div id="header-top">
			<img src="https://scontent-mxp1-1.xx.fbcdn.net/v/t39.30808-6/274727807_344679267656723
					_4101110072475819472_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=Jn3P2n6
					aCRoQ7kNvgFrToKU&_nc_zt=23&_nc_ht=scontent-mxp1-1.xx&_nc_gid=Avo6WH1i8umjYnI5b
					SOnK85&oh=00_AYCyNv31Tdh6rmjndaGBkDycKzpG7JXBTOOCG2P0BuAm2g&oe=67345ED1" />
			<h1 class="vmaps">VMAPS</h1>
		</div>
		<div id ="companyname">
			<h1 id="telmekon">Telmekon</h1>
		</div>

</div>


<div id="content">


	<div class="" id="netname"></div>
		<div class="flex flex-col items-center">
			<button class = "focus:outline-none text-white bg-red-800 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-900" id ="scan" on:click={() => show = !show}>Analyze</button>

		</div>
	{#if !show}
	<div class="items-center flex">
		<div class="flex flex-cols-3 gap-3 ml-3 items-center flex-wrap ">
		{#each Object.entries(data) as [key, object]}
			<div>
			<a href="#" class="block max-w-sm p-6 bg-red-600 border border-gray-200 rounded-lg shadow dark:bg-{color}-700 dark:border-red-500">
				<p class="font-normal text-white dark:text-white">
				{#each Object.entries(object) as [key2, value]}

					{key2}: {value}
				{/each}
				</p>
			</a>
			</div>
		{/each}
		</div>
	</div>
	{/if}
</div>






<style>

		*{
				height: 100%;
				width: auto;
		}

		#header {
				margin: 50px;
				width: 100%;
		}

		h1 {
        font-size: 20px;
        font-family: "Afacad";

    }

		#companyname{

				margin-bottom: 30px;
		}
		#netname{
				width: 100%;
		}
		#scan{
				margin: 0 auto;
				height: 80px;
				width: 160px;
				margin-bottom: 20px;
				border-radius: 15px;
		}
		#telmekon{

				margin-top: 20px;
				margin-left: 20px;
		}
		img {
				height: 150px;
				border-radius: 50%;
				border: 1px solid black;
		}

		#header-top{
				width: 100%;
				display: flex;
				flex-wrap: wrap;
				align-content: space-between;

		}

		.vmaps{
				font-size: 100px;
				margin: 0 auto;
		}



</style>


