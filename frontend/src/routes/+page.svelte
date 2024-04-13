<script lang="ts">
  import { Button, ButtonGroup, Heading } from 'flowbite-svelte';
</script>

<div class="w-screen h-screen flex justify-center place-content-center">
  <div class="flex flex-col place-content-center">
    <div class="w-[65ch] flex flex-col gap-4">
      <Heading tag="h1" class="text-4xl text-center text-black">Choose a Patient</Heading>
      <Button href="/" size="lg" color="light" class="mx-4 hover:ml-8 hover:mr-0 hover:bg-white hover:shadow hover:font-bold transition-all" pill>Patient 1</Button>
      <Button href="/" size="lg" color="light" class="mx-4 hover:ml-8 hover:mr-0 hover:bg-white hover:shadow hover:font-bold transition-all" pill>Patient 2</Button>
      <Button href="/" size="lg" color="light" class="mx-4 hover:ml-8 hover:mr-0 hover:bg-white hover:shadow hover:font-bold transition-all" pill>Patient 3</Button>
      <Button href="/" size="lg" color="light" class="mx-4 hover:ml-8 hover:mr-0 hover:bg-white hover:shadow hover:font-bold transition-all" pill>Patient 4</Button>
    </div>
  </div>
</div>
