export type SelectItem = {
  href: string;
  label: string;
}

export type Patient = {
  id: string;
  name: string;
  id_string: string;
}

export type Pair = {
  id: string;
  patient_id: string;
  object_one_type: string;
  object_one_value: string;
  object_two_type: string;
  object_two_value: string;
}
