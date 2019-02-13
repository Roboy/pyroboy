import face_recognition as fr
import math
import numpy as np

class FaceRec:

    def face_distance_to_conf(face_distance, face_match_threshold=0.6):
        if face_distance > face_match_threshold:
            range = (1.0 - face_match_threshold)
            linear_val = (1.0 - face_distance) / (range * 2.0)
            return linear_val
        else:
            range = face_match_threshold
            linear_val = 1.0 - (face_distance / (range * 2.0))
            return linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))

    def get_biggest_face_encoding(img_path):
        loaded_img = fr.load_image_file(img_path)
        face_encodings = fr.face_encodings(loaded_img)
        if len(face_encodings) == 0:
            return None

        face_locations = fr.face_locations(loaded_img)
        face_sizes = []
        for (top, right, bottom, left) in face_locations:
            x = np.array((left, top))
            y = np.array((right, bottom))
            face_sizes.append(np.linalg.norm(x-y))
        index_biggest = np.argmax(face_sizes)
        return face_encodings[index_biggest]

    def match_face(new_face, known_faces, face_match_threshold=0.6):
        '''
        returns the closest face index from known_faces and confidence in [0,1]
        '''
        distances = fr.face_distance(known_faces, new_face)
        confidences = [FaceRec.face_distance_to_conf(d, face_match_threshold=face_match_threshold) for d in distances]
        index_max = np.argmax(confidences)#max(xrange(len(confindences)), key=confindences.__getitem__)
        print("max index: %i"%index_max)
        # print("conf: %d"%confidences[index_max])
        return index_max, confidences[index_max]
