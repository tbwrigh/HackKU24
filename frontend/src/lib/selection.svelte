<script lang="ts">
  import { Button, Heading } from 'flowbite-svelte';

  export let heading;
  export let options: string[];
</script>

<div class="w-screen h-screen flex justify-center place-content-center">
  <div class="flex flex-col place-content-center">
    <div class="w-[65ch] flex flex-col gap-4">
      <Heading tag="h1" class="text-4xl text-center text-black">{heading}</Heading>
      {#each options as option}
        <Button href="/" size="lg" color="light" class="mx-4 hover:ml-8 hover:mr-0 hover:bg-white hover:shadow hover:font-bold transition-all" pill>{option}</Button>
      {/each}
    </div>
  </div>
</div>
