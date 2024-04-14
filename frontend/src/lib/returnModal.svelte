<script lang="ts">
    import { page } from '$app/stores';
  import { Heading, Modal, Button } from 'flowbite-svelte';

  export let open: boolean;
  export let route: string;

  const properName: string = route[0].toUpperCase() + route.slice(1, route.length);
</script>

<Modal bind:open={open} class="bg-transparent">
    <Heading>Congratulations! You completed the {properName}!</Heading>
    <Button color="purple" on:click={() => {window.location.reload()}}>Restart</Button>
    <Button color="blue" on:click={() => {window.location.href =  `/patient/${$page.params.slug}/${route}`}}>Back to {properName}</Button>
    <Button color="red" on:click={() => {window.location.href =  `/patient/${$page.params.slug}`}}>Back to Games</Button>
</Modal>
