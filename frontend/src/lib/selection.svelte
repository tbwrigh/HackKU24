<script lang="ts">
  import { Button, Heading } from 'flowbite-svelte';
  import type { SelectItem } from './types';

  export let heading: string;
  export let options: SelectItem[];
</script>

<div class="flex w-dvw h-dvh justify-center items-center place-content-center">
  <div class="w-[65ch] flex flex-col gap-4">
    <Heading tag="h1" class="text-4xl text-center text-black">{heading}</Heading>
    {#each options as option}
      <Button href={option.href} size="lg" color="light" class="mx-4 hover:ml-8 hover:mr-0 hover:bg-white hover:shadow hover:font-bold transition-all" pill>{option.label}</Button>
    {/each}
  </div>
</div>
