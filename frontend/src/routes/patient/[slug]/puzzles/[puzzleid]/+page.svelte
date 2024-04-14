<script lang="ts">
    import { onMount } from 'svelte';
    import { page } from '$app/stores';

    import { ArrowLeftOutline } from 'flowbite-svelte-icons';
    import { Heading } from 'flowbite-svelte';

    const backendUrl = import.meta.env.VITE_BACKEND_URL;


    let blob: Blob | undefined;
    let filename: string | undefined;
    let title: string | undefined;
    let imageUrl: string | undefined;

    let numColumns = 2;
    let numRows = 2;

    onMount(async () => {
        console.log('Puzzles page mounted');
        const res = await fetch(`${backendUrl}/puzzle/${$page.params.puzzleid}`)
        const data = await res.json();
        filename = data.filename;
        title = data.name;

        const res2 = await fetch(`${backendUrl}/patient/${$page.params.slug}/download/${data.filename}`);
        blob = await res2.blob();    
        imageUrl = URL.createObjectURL(blob);

        const canvas = document.getElementById('puzzle') as HTMLCanvasElement;

        const image = new Image();
        image.src = imageUrl;

        image.onload = () => {
            const ctx = canvas.getContext('2d');
            if (ctx === null) {
                console.error('Could not get 2d context');
                return;
            };

            let scale = 0.75;

            canvas.width = image.width *scale;
            canvas.height = image.height *scale;

            const pieceWidth = (image.width  * scale)/ numColumns;
            const pieceHeight = (image.height  * scale)/ numRows;

            for (let x = 0; x < numColumns; x++) {
                for (let y = 0; y < numRows; y++) {
                    ctx.drawImage(image, x * pieceWidth / scale, y * pieceHeight / scale, pieceWidth / scale, pieceHeight / scale, x * pieceWidth, y * pieceHeight, pieceWidth, pieceHeight);
                    ctx.strokeStyle = 'black';
                    ctx.strokeRect(x*pieceWidth, y*pieceHeight, (x+1)*pieceWidth, (y+1)*pieceHeight);
                }
            }
        }
    });
</script>

<div class="flex w-full h-screen justify-center items-start pt-30">
    <div class="w-[65ch] flex flex-col gap-4 mt-20">

        <Heading level={1} class="text-4xl text-center text-black">
            {#if imageUrl}
            Puzzle: {title}
            {:else}
            Loading...
            {/if}

        </Heading>

        <canvas id="puzzle" class="w-auto h-auto max-w-full max-h-full justify-center"></canvas>
    </div>
</div>
