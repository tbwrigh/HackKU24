import type { PageLoad } from './$types';

const backendUrl = import.meta.env.VITE_BACKEND_URL;

export const load: PageLoad = async ({ fetch, params }) => {
  let json: null | JSON = null;
  try {
    const response = await fetch(`${backendUrl}/content/get_pairs_by_patient_id_pair_patient_id_get`);
    json = await response.json();
  } catch (error) {
    console.error('Error:', error);
  }
  return {
    pairs: json
  };
};
