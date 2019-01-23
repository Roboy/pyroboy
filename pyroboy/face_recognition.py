import face_recognition as fr

class FaceRec:

    def get_face_encoding(img_path):
        loaded_img = fr.load_image_file(img_path)
        return fr.face_encodings(loaded_img)[0]

    def match_face(new_face, known_faces, tolerance=0.5):
        '''
        returns the first index of the known_faces that matches new_face
        with given tolerance
        '''
        match = fr.compare_faces(known_faces, new_face, tolerance=tolerance)
        idx = None
        try:
            idx = match.index(True)
        except:
            pass
        return idx
