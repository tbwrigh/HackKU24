<script lang="ts">
    import type { PageData } from './$types';
    import { onMount } from 'svelte';

    import { PlusOutline } from 'flowbite-svelte-icons';
    import { Button, Modal, Select, Input, Label } from 'flowbite-svelte';

    import PairComponent from '$lib/PairComponent.svelte';

    import type { Patient } from '$lib/types';
  
    const backendUrl = import.meta.env.VITE_BACKEND_URL;

    export let data: PageData;

    let patient: Patient = {
        name: "",
        id: "",
        id_string: "",
    };

    let pairs: string[] = [];

    onMount(async () => {
        const res = await fetch(`${backendUrl}/patient/${data.slug}`);
        patient = await res.json();
        const res2 = await fetch(`${backendUrl}/pair/patient/${patient.id}`);
        let pairsData = await res2.json();
        pairsData.forEach((pair: any) => {
            pairs = [...pairs, pair.id];
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
  </script>

    <h1>{patient.name}'s Profile</h1>

    <div class="grid grid-cols-1 gap-4 mt-4">
        {#each pairs as pair (pair)}
            <PairComponent id={pair} deleteCallback={deleteCallback}/>
        {/each}
    </div>


    <div class="fixed bottom-4 right-4 z-50">
        <Button on:click={() => (addModal = true)} color="blue" pill={true} class="!p-2">
          <PlusOutline class="w-8 h-8"/>
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