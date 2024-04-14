<script lang="ts">
    import type { PageData } from './$types';
    import { onMount } from 'svelte';

    import { ArrowLeftOutline, FileCopyOutline, GridOutline } from 'flowbite-svelte-icons';
    import { Button, Modal, Select, Input, Label, Heading, SpeedDial, SpeedDialButton } from 'flowbite-svelte';

    import PairComponent from '$lib/PairComponent.svelte';
    import PuzzleComponent from '$lib/PuzzleComponent.svelte';

    import type { Patient } from '$lib/types';
  
    const backendUrl = import.meta.env.VITE_BACKEND_URL;

    export let data: PageData;

    let patient: Patient = {
        name: "",
        id: "",
        id_string: "",
    };

    let activeTab = 'pairs';

    function switchTab(tab: string) {
        activeTab = tab;
    }

    let pairs: string[] = [];

    let puzzles: string[] = [];

    onMount(async () => {
        const res = await fetch(`${backendUrl}/patient/${data.slug}`);
        patient = await res.json();
        
        const res2 = await fetch(`${backendUrl}/pair/patient/${patient.id}`);
        let pairsData = await res2.json();
        pairsData.forEach((pair: any) => {
            pairs = [...pairs, pair.id];
        });

        const res3 = await fetch(`${backendUrl}/puzzle/patient/${patient.id}`);
        let puzzlesData = await res3.json();
        puzzlesData.forEach((puzzle: any) => {
            puzzles = [...puzzles, puzzle.id];
        });
    });

    let addModal = false;
    let leftSelection = 'string'; 
    let rightSelection = 'string';

    async function onSubmit(event: any) {
        event.preventDefault();

        const formData = new FormData(event.target);

        console.log(formData);

        const sendData = new FormData();

        if (formData.get('leftInput') == null || formData.get('rightInput') == null) {
            alert('Please fill out all fields');
            return;
        }

        if (leftSelection === 'string') {
            sendData.append('object_one_value', formData.get('leftInput')?.toString() || '');
        } else {
            sendData.append('object_one_value', formData.get('leftInput') as File);
        }

        if (rightSelection === 'string') {
            sendData.append('object_two_value', formData.get('rightInput')?.toString() || '');
        } else {
            sendData.append('object_two_value', formData.get('rightInput') as File);
        }

        const res = await fetch(`${backendUrl}/pair/${patient.id}`, {
            method: 'POST',
            body: sendData,
        });

        if (!res.ok) {
            throw new Error('Network response was not ok');
        }

        pairs = [...pairs, (await res.json()).id];

        addModal = false;
        leftSelection = 'string';
        rightSelection = 'string';
        console.log('submitted');
    }

    async function deleteCallback(id: string) {
        let temp_pairs: string[] = pairs.filter((pair) => pair !== id);
        pairs = temp_pairs;
    }

    async function deleteCallbackPuzzle(id: string) {
        console.log('deleting puzzle');
        console.log(puzzles)
        let temp_puzzles: string[] = puzzles.filter((puzzle) => puzzle !== id);
        console.log(temp_puzzles);
        puzzles = temp_puzzles;
    }

    async function deletePatient() {
        const res = await fetch(`${backendUrl}/patient/${patient.id}`, {
            method: 'DELETE',
        });

        if (!res.ok) {
            throw new Error('Network response was not ok');
        }

        window.location.href = '/';
    }

    let addPuzzleModal = false;

    async function onPuzzleSubmit(event: any) {
        event.preventDefault();

        const formData = new FormData(event.target);

        console.log(formData);

        const sendData = new FormData();

        if (formData.get('puzzleName') == null || formData.get('puzzleFile') == null) {
            alert('Please fill out all fields');
            return;
        }

        sendData.append('name', formData.get('puzzleName')?.toString() || '');
        sendData.append('file', formData.get('puzzleFile') as File);

        const res = await fetch(`${backendUrl}/puzzle/${patient.id}`, {
            method: 'POST',
            body: sendData,
        });

        if (!res.ok) {
            throw new Error('Network response was not ok');
        }

        puzzles = [...puzzles, (await res.json()).id];

        addPuzzleModal = false;
        console.log('submitted');
    
    }
</script>

<div class="flex w-full h-screen justify-center items-start pt-30">
    <div class="w-[65ch] flex flex-col gap-4">
        <div class="flex items-center justify-start sticky top-20 z-10 w-full">
            <a href={`/patient/${patient.id}`}>
                <ArrowLeftOutline class="w-12 h-12 text-gray-200" />
            </a>
            <Heading level={1} class="text-4xl text-center text-white">
                {patient.name}'s Profile
            </Heading>
        </div>

        <div class="flex border-b mt-[5rem]">
            <button class={`py-2 px-4 text-white ${activeTab === 'pairs' ? 'border-b-2 border-blue-500' : ''}`} on:click={() => switchTab('pairs')}>
              Pairs
            </button>
            <button class={`py-2 px-4 text-white ${activeTab === 'puzzles' ? 'border-b-2 border-blue-500' : ''}`} on:click={() => switchTab('puzzles')}>
              Puzzles
            </button>
          </div>

        <div class="overflow-y-auto max-h-[80vh]">
            {#if activeTab === 'pairs'}
            <div class="grid grid-cols-1 gap-4">
                {#each pairs as pair (pair)}
                <PairComponent id={pair} deleteCallback={deleteCallback}/>
                {/each}
            </div>
            {:else}
                {#each puzzles as puzzle (puzzle)}
                <PuzzleComponent id={puzzle} deleteCallback={deleteCallbackPuzzle}/>
                {/each}
            {/if}
        </div>
    </div>
</div>

<SpeedDial class="fixed bottom-4, right-4 z-50" color="blue">
    <SpeedDialButton name="Add Pair" color="blue" on:click={() => {addModal = true}}>
        <FileCopyOutline class="w-5 h-5" />
    </SpeedDialButton>
    <SpeedDialButton name="Add Puzzle" color="blue" on:click={() => {addPuzzleModal = true}}>
        <GridOutline class="w-5 h-5" />
    </SpeedDialButton>
</SpeedDial>


<div class="fixed bottom-4 left-4 z-50">
    <Button on:click={deletePatient} color="red" class="!p-2">
        Delete Patient
    </Button>
</div>
<Modal bind:open={addModal} size="md" autoclose={false} class="w-full">
    <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Add a Pair</h3>
    <form class="p-4" on:submit={onSubmit}>
        <div class="grid grid-cols-2 gap-4">
          <div class="flex flex-col">
            <Label for="leftSelection" class="mb-2 w-full">
                Select Type (left)
            </Label>
            <Select bind:value={leftSelection} class="w-full mb-2">
              <option value="string">String</option>
              <option value="file">File</option>
            </Select>
            {#if leftSelection === 'string'}
                <Label for="leftInput" class="mb-2 w-full">
                    Enter Text (right)
                </Label>
                <Input name="leftInput" id="leftInput" type="text" placeholder="Enter string" class="w-full" required/>
            {:else}
                <Label for="leftInput" class="mb-2 w-full">
                    Upload File (right)
                </Label>
                <Input name="leftInput" id="leftInput" type="file" class="w-full" required/>
            {/if}
          </div>
          <div class="flex flex-col">
            <Label for="rightSelection" class="mb-2 w-full">
                Select Type (left)
            </Label>
            <Select bind:value={rightSelection} class="w-full mb-2">
              <option value="string">String</option>
              <option value="file">File</option>
            </Select>
            {#if rightSelection === 'string'}
                <Label for="rightInput" class="mb-2 w-full">
                    Enter Text (right)
                </Label>
                <Input name="rightInput" id="rightInput" type="text" placeholder="Enter string" class="w-full" required/>
            {:else}
                <Label for="rightInput" class="mb-2 w-full">
                    Upload File (right)
                </Label>
                <Input name="rightInput" id="rightInput" type="file" class="w-full" required/>
            {/if}
          </div>
        </div>
      
        <Button type="submit" class="w-full mt-4" color="blue">Submit</Button>
      </form>
</Modal>

<Modal bind:open={addPuzzleModal} size="md" autoclose={false} class="w-full">
    <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Add a Puzzle</h3>
    <form class="p-4" on:submit={onPuzzleSubmit}>
        <Label for="puzzleName" class="mb-2 w-full">
            Puzzle Name
        </Label>
        <Input name="puzzleName" id="puzzleName" type="text" placeholder="Enter puzzle name" class="w-full" required/>
        <br>
        <Label for="puzzleFile" class="mb-2 w-full">
            Upload Puzzle File
        </Label>
        <Input name="puzzleFile" id="puzzleFile" type="file" class="w-full" required/>
        <br>
        <Button type="submit" class="w-full mt-4" color="blue">Submit</Button>
    </form>
</Modal>
