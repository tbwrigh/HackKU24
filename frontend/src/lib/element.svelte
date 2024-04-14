<script lang="ts">
  import type { Pair } from '$lib/types.ts';

  export let pair: Pair;
  export let one_or_two: number;
</script>

<div>
  {#if one_or_two==1 && pair.object_one_type=="file"}
    <img src={pair.object_one_value} />
  {:else if one_or_two==1 && pair.object_one_type=="string"}
    <p>{pair.object_one_value}</p>
  {:else if one_or_two==2 && pair.object_two_type=="file"}
    <img src={pair.object_two_value} />
  {:else if one_or_two==2 && pair.object_two_type=="string"}
    <p>{pair.object_two_value}</p>
  {:else}
    <p>unrecognized element type</p>
  {/if}
</div>
