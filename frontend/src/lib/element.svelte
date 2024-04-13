<script lang="ts">
  import { ElementType } from '$lib/types.ts';

  export let type: ElementType;
  export let value: string;
</script>

<div>
  {#if type==ElementType.Image}
    <img src={value} />
  {:else if type==ElementType.Text}
    <p>{value}</p>
  {:else}
    <p>unrecognized element type</p>
  {/if}
</div>
