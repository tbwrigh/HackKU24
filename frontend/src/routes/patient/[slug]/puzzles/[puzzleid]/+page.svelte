<script lang="ts">
    import { onMount } from 'svelte';
    import { page } from '$app/stores';
    import { Heading } from 'flowbite-svelte';
    import ReturnModal from '$lib/returnModal.svelte';

    const backendUrl = import.meta.env.VITE_BACKEND_URL;


    let blob: Blob | undefined;
    let filename: string | undefined;
    let title: string | undefined;
    let imageUrl: string | undefined;

    let numColumns = 3;
    let numRows = 3;

    type AnswerBox = {
        x: number;
        y: number;
        width: number;
        height: number;
        q: number;
    }

    let answerBoxes: AnswerBox[] = [];
    let puzzleBoxes: AnswerBox[] = [];
    let completed: number[] = [];

    type SelectedBox = {
        answerBox: boolean;
        q: number;
    }

    let shouldShuffle = true;
    let coords: any[] = [];

    let complete = false;

    let selected: SelectedBox | undefined;

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
        
        let updateCanvas = () => {
            const ctx = canvas.getContext('2d');
            if (ctx === null) {
                console.error('Could not get 2d context');
                return;
            };

            canvas.width = window.innerWidth * 1;
            canvas.height = window.innerHeight * 1;

            let scale = 0.25;

            if (image.width > canvas.width || image.height > canvas.height) {
                scale = Math.min(canvas.width / image.width, canvas.height / image.height) / 2;
            }else {
                scale = Math.min(canvas.width / image.width, canvas.height / image.height) / 2;
            }

            console.log('scale', scale);

            const pieceWidth = (image.width  * scale)/ numColumns;
            const pieceHeight = (image.height  * scale)/ numRows;

            let x_offset = (canvas.width - pieceWidth * numColumns) / 2;

            for (let x = 0; x < numColumns; x++) {
                for (let y = 0; y < numRows; y++) {
                    // ctx.drawImage(image, x * pieceWidth / scale, y * pieceHeight / scale, pieceWidth / scale, pieceHeight / scale, x_offset + x * pieceWidth, y * pieceHeight, pieceWidth, pieceHeight);
                    if (completed.includes(x + y * numColumns)) {
                        ctx.drawImage(image, x * pieceWidth / scale, y * pieceHeight / scale, pieceWidth / scale, pieceHeight / scale, x_offset + x * pieceWidth, y * pieceHeight, pieceWidth, pieceHeight);
                    }else {
                        answerBoxes.push({x: x_offset + x * pieceWidth, y: y * pieceHeight, width: pieceWidth, height: pieceHeight, q: x + y * numColumns});
                    }
                    ctx.strokeStyle = 'white';
                    ctx.strokeRect(x_offset + x * pieceWidth, y * pieceHeight, pieceWidth, pieceHeight);
                }
            }



            let y_offset = (pieceHeight * numRows)*1.1;
            let spacing = 0.1* pieceWidth;
            let vspace = 0.1* pieceHeight;
            let row_height = pieceHeight + vspace;
            let row = 0;

            // scramble coords
            if (shouldShuffle) {
                for (let x = 0; x < numColumns; x++) {
                    for (let y = 0; y < numRows; y++) {
                        coords.push({x: x, y: y});
                    }
                }
                coords.sort(() => Math.random() - 0.5);
                shouldShuffle = false;
            }
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
                if (completed.includes(positionIndex)) {
                    continue;
                }else {
                    ctx.drawImage(image, x * pieceWidth / scale, y * pieceHeight / scale, pieceWidth / scale, pieceHeight / scale, (q - row * row_width) * (pieceWidth+spacing), y_offset + row * row_height, pieceWidth, pieceHeight);
                    puzzleBoxes.push({x: (q - row * row_width) * (pieceWidth+spacing), y: y_offset + row * row_height, width: pieceWidth, height: pieceHeight, q: positionIndex});
                }
                ctx.strokeRect((q - row * row_width) * (pieceWidth+spacing), y_offset + row * row_height, pieceWidth, pieceHeight);
            }

            if (selected) {
                ctx.fillStyle = 'rgba(0, 255, 0, 0.5)';

                let tbox = undefined;
                if (selected.answerBox) {
                    tbox = answerBoxes.filter((box) => box.q == selected?.q)[0];
                }else {
                    tbox = puzzleBoxes.filter((box) => box.q == selected?.q)[0];
                }

                if (tbox) {
                    ctx.fillRect(tbox.x, tbox.y, tbox.width, tbox.height);
                }
            }

            if (completed.length == numColumns*numRows) {
                complete = true;
            }

        }

        image.onload = () => {
            updateCanvas();
        }

        canvas.addEventListener('click', (e) => {
            console.log('click');
            console.log(answerBoxes)

            const rect = canvas.getBoundingClientRect();
            let x = e.clientX - rect.left;
            let y = e.clientY - rect.top;

            x *= canvas.width / rect.width;
            y *= canvas.height / rect.height;

            for (let i = 0; i < answerBoxes.length; i++) {
                if (x >= answerBoxes[i].x && x <= answerBoxes[i].x + answerBoxes[i].width && y >= answerBoxes[i].y && y <= answerBoxes[i].y + answerBoxes[i].height) {
                    console.log('Answer box', answerBoxes[i].q);
                    selectBox(true, answerBoxes[i].q);
                    return;
                }
            }

            for (let i = 0; i < puzzleBoxes.length; i++) {
                if (x >= puzzleBoxes[i].x && x <= puzzleBoxes[i].x + puzzleBoxes[i].width && y >= puzzleBoxes[i].y && y <= puzzleBoxes[i].y + puzzleBoxes[i].height) {
                    console.log('Puzzle box', puzzleBoxes[i].q);
                    selectBox(false, puzzleBoxes[i].q);
                    return;
                }
            }

            selected = undefined;
            console.log('x', x, 'y', y);
            updateCanvas();
        });

        function selectBox(answerBox: boolean, q: number) {
            if (selected) {
                if (selected.answerBox == answerBox) {
                    if (completed.includes(q)) {
                        updateCanvas();
                        return;
                    }
                    selected = {
                        answerBox: answerBox,
                        q: q
                    };
                    updateCanvas();
                    return;
                }else if (selected.q == q) {
                    completed.push(q);
                    selected = undefined;
                    updateCanvas();
                    return;
                }else {
                    selected = undefined;
                    updateCanvas();
                    return;
                }
            }else {
                if (completed.includes(q)) {
                    updateCanvas();
                    return;
                }
                selected = {
                    answerBox: answerBox,
                    q: q
                };
                updateCanvas();
            }
        }
    });
</script>

<div class="flex w-full h-screen justify-center items-center pt-30">
    <div class="w-[65ch] flex flex-col gap-4 mt-20">

        <Heading level={1} class="text-4xl text-center text-white">
            {#if imageUrl}
            Puzzle: {title}
            {:else}
            Loading...
            {/if}

        </Heading>

        <canvas id="puzzle" class="w-auto h-auto max-w-full max-h-full justify-center"></canvas>
    </div>
</div>

  <ReturnModal open={complete} route={"puzzles"} />
