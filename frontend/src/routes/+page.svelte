<script lang="ts">
  import Selection from '$lib/selection.svelte';
  import { Button, Modal, Label, Input } from 'flowbite-svelte';
  import { PlusOutline } from 'flowbite-svelte-icons';
  let formModal = false;

  const backendUrl = import.meta.env.VITE_BACKEND_URL;

  async function handleSubmit(event: any) {
    event.preventDefault();

    console.log(event.target);

    const formData = new FormData(event.target);

    console.log(formData); 

    const patientName: string = formData.get('patientName')?.toString() || '';

    if (!patientName) {
      alert('Please enter a patient name');
      return;
    }

    const id_string = btoa(patientName)
      .replace(/=/g, '')
      .replace(/\+/g, '_')
      .replace(/\//g, '_')
      .toLowerCase();
    
    try {
      const response = await fetch(`${backendUrl}/patient/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ id_string: id_string, name: patientName }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      formModal = false;
      location.reload();
    } catch (error) {
      console.error('Error:', error);
    }
  }
</script>

<Selection heading={"Choose a Patient"} options={["Bob", "Janet", "Ivan", "Dorothy"]} />

<div class="fixed bottom-4 right-4 z-50">
  <Button on:click={() => (formModal = true)} color="blue" pill={true} class="!p-2">
    <PlusOutline class="w-8 h-8"/>
  </Button>
</div>

<Modal bind:open={formModal} size="md" autoclose={false} class="w-full">
  <form class="flex flex-col space-y-6" on:submit={handleSubmit}>
    <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Add a Patient</h3>
    <Label class="space-y-2">
      <span>Patient Name</span>
      <Input name="patientName" type="text" placeholder="Enter patient name" required />
    </Label>
    <br>
    <Button type="submit" class="w-full1" color="blue">
      Submit
    </Button>
  </form>
</Modal>