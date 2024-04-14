def delete_file(gcs_client, patient_id, filename):
    bucket = gcs_client.get_bucket(patient_id)
    blob = bucket.blob(filename)
    blob.delete()

def upload_file(gcs_client, patient_id, file):
    bucket = gcs_client.get_bucket(patient_id)
    filenames = [blob.name for blob in bucket.list_blobs()]
    i = 0
    original_filename = file.filename
    while file.filename in filenames:
        file.filename = f"{i}_{original_filename}"
        i += 1
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file.file)
    return file.filename

