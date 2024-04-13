<script lang="ts">
  import Selection from '$lib/selection.svelte';
  import { Button, Modal, Label, Input } from 'flowbite-svelte';
  import { PlusOutline } from 'flowbite-svelte-icons';
  let formModal = false;
</script>

<Selection heading={"Choose a Patient"} options={["Bob", "Janet", "Ivan", "Dorothy"]} />

<div class="fixed bottom-4 right-4 z-50">
  <Button on:click={() => (formModal = true)} color="blue" pill={true} class="!p-2">
    <PlusOutline class="w-8 h-8"/>
  </Button>
</div>

<Modal bind:open={formModal} size="md" autoclose={false} class="w-full">
  <form class="flex flex-col space-y-6" action="#">
    <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Add a Patient</h3>
    <Label class="space-y-2">
      <span>Patient Name</span>
      <Input type="text" placeholder="Enter patient name" required />
    </Label>
    <br>
    <Button type="submit" class="w-full1" color="blue">
      Submit
    </Button>
  </form>
</Modal>