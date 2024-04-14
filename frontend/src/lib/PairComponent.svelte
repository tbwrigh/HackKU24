<script lang="ts">
    import { onMount } from 'svelte';
    import { Button } from 'flowbite-svelte'; // Import Flowbite components
    import { TrashBinOutline } from 'flowbite-svelte-icons';

    const backendUrl = import.meta.env.VITE_BACKEND_URL;

    export let id: string;  // Receive `id` as a prop

    export let deleteCallback: any;
  
    let leftText = '';
    let rightText = '';
  
    onMount(async () => {
      try {
        const response = await fetch(`${backendUrl}/pair/${id}`);
        if (response.ok) {
          const data = await response.json();
          leftText = data.object_one_value;  
          rightText = data.object_two_value; 
        } else {
          console.error('Failed to fetch data');
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    });
  
    async function handleDelete() {
        await fetch(`${backendUrl}/pair/${id}`, {
            method: 'DELETE',
        }).then((response) => {
            if (response.ok) {
                console.log(`Successfully deleted item with ID: ${id}`);
                deleteCallback(id);
            } else {
                console.error(`Failed to delete item with ID: ${id}`);
            }
        }).catch((error) => {
            console.error('Error deleting item:', error);
        });
    }
  </script>
  
  <div class="flex justify-between items-center border-2 border-white shadow-md p-4 rounded-lg">
    <div class="flex-grow text-white" style="flex-basis: 0%; max-width: 45%;">{leftText}</div>
    <div class="flex-grow text-white" style="flex-basis: 0%; max-width: 45%;">{rightText}</div>  
    <Button class="w-1/10" color="blue" size="xs" on:click={handleDelete}>
      <TrashBinOutline/>
    </Button>
  </div>
