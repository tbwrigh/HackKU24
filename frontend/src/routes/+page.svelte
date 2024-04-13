<script lang="ts">
  import { Alert, Label, Input } from 'flowbite-svelte';
  import { ElementType } from '$lib/types.ts';
  import Element from '$lib/element.svelte';

  let in0val = "";
  let in1val = "";
</script>

<div>
  <Label for="default-input" class="block mb-2">Item 1</Label>
  <Input id="default-input" name="in0" placeholder="first match" bind:value={in0val} />
  <Label for="default-input" class="block mb-2">Item 2</Label>
  <Input id="default-input" name="in1" placeholder="second match" bind:value={in1val} />
  {#if in0val!=="" && in0val==in1val}
    <Alert>They match!</Alert>
  {/if}
</div>

<Element value={"hello!"} type={ElementType.Text}/>
