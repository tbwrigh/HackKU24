<script lang="ts">
    import type { PageData } from './$types';
    import { onMount } from 'svelte';

    import { PlusOutline } from 'flowbite-svelte-icons';
    import { Button, Modal, Select, Input, Label } from 'flowbite-svelte';

    import type { Patient } from '$lib/types';
  
    const backendUrl = import.meta.env.VITE_BACKEND_URL;

    export let data: PageData;

    let patient: Patient = {
        name: "",
        id: "",
        id_string: "",
    };

    onMount(async () => {
        console.log(data);
        console.log(data.slug);
        console.log(`${backendUrl}/patients/${data.slug}`);
        const res = await fetch(`${backendUrl}/patient/${data.slug}`);
        patient = await res.json();
    });

    let addModal = false;
    let leftSelection = 'string'; 
    let rightSelection = 'string';

    
  </script>

    <h1>{patient.name}'s Profile</h1>

    <div class="fixed bottom-4 right-4 z-50">
        <Button on:click={() => (addModal = true)} color="blue" pill={true} class="!p-2">
          <PlusOutline class="w-8 h-8"/>
        </Button>
      </div>
      

<Modal bind:open={addModal} size="md" autoclose={false} class="w-full">
    <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Add a Pair</h3>
    <form class="p-4">
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
                <Input id="leftInput" type="text" placeholder="Enter string" class="w-full"/>
            {:else}
                <Label for="leftInput" class="mb-2 w-full">
                    Upload File (right)
                </Label>
                <Input id="leftInput" type="file" class="w-full"/>
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
                <Input id="rightInput" type="text" placeholder="Enter string" class="w-full"/>
            {:else}
                <Label for="rightInput" class="mb-2 w-full">
                    Upload File (right)
                </Label>
                <Input id="rightInput" type="file" class="w-full"/>
            {/if}
          </div>
        </div>
      
        <Button type="submit" class="w-full mt-4" color="blue">Submit</Button>
      </form>
</Modal>