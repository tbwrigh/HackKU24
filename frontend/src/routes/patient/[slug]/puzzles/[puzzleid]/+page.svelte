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

    let numColumns = 3;
    let numRows = 3;

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

            // canvas.width = image.width;
            // canvas.height = image.height;
            canvas.width = window.innerWidth * 0.8;
            canvas.height = window.innerHeight * 0.8;

            let scale = 0.25;

            if (image.width > canvas.width || image.height > canvas.height) {
                scale = Math.min(canvas.width / image.width, canvas.height / image.height) / 2;
            }


            console.log('scale', scale);

            const pieceWidth = (image.width  * scale)/ numColumns;
            const pieceHeight = (image.height  * scale)/ numRows;

            let x_offset = (canvas.width - pieceWidth * numColumns) / 2;

            for (let x = 0; x < numColumns; x++) {
                for (let y = 0; y < numRows; y++) {
                    // ctx.drawImage(image, x * pieceWidth / scale, y * pieceHeight / scale, pieceWidth / scale, pieceHeight / scale, x_offset + x * pieceWidth, y * pieceHeight, pieceWidth, pieceHeight);
                    ctx.strokeStyle = 'black';
                    ctx.strokeRect(x_offset + x * pieceWidth, y * pieceHeight, pieceWidth, pieceHeight);
                }
            }

            let coords = [];
            for (let x = 0; x < numColumns; x++) {
                for (let y = 0; y < numRows; y++) {
                    coords.push({x: x, y: y});
                }
            }

            let y_offset = (pieceHeight * numRows)*1.1;
            let spacing = 0.1* pieceWidth;
            let vspace = 0.1* pieceHeight;
            let row_height = pieceHeight + vspace;
            let row = 0;

            // scramble coords
            coords.sort(() => Math.random() - 0.5);
            let row_width = -1;

            for (let q = 0; q < numColumns*numRows; q++) {
                let x = coords[q].x;
                let y = coords[q].y;
                let positionIndex = x + y * numColumns;
                if ((q+2 - row * q)*(pieceWidth + spacing) > canvas.width) {
                    row++;
                    if (row_width == -1) {
                        row_width = q;
                    }
                }
                ctx.drawImage(image, x * pieceWidth / scale, y * pieceHeight / scale, pieceWidth / scale, pieceHeight / scale, (q - row * row_width) * (pieceWidth+spacing), y_offset + row * row_height, pieceWidth, pieceHeight);
                ctx.strokeRect((q - row * row_width) * (pieceWidth+spacing), y_offset + row * row_height, pieceWidth, pieceHeight);
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

        <canvas id="puzzle" class="w-[80vw] h-[80vh] justify-center"></canvas>
    </div>
</div>
