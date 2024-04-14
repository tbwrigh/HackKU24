<script lang="ts">
    import { page } from '$app/stores';
  import { Heading, Modal, Button } from 'flowbite-svelte';

  export let open: boolean;
  export let route: string;

  const properName: string = route[0].toUpperCase() + route.slice(1, route.length);
</script>

<Modal bind:open={open} class="dark:bg-transparent dark:shadow-none">
    <Heading class="text-center py-4">Congratulations! You completed the {properName}!</Heading>
  <div class="flex flex-row gap-4">
    <Button class="basis-full" color="purple" on:click={() => {window.location.reload()}}>Restart</Button>
    <Button class="basis-full" color="blue" on:click={() => {window.location.href =  `/patient/${$page.params.slug}/${route}`}}>Back to {properName}</Button>
    <Button class="basis-full" color="red" on:click={() => {window.location.href =  `/patient/${$page.params.slug}`}}>Back to Games</Button>
    </div>
</Modal>
