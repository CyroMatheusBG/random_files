from pdf2image import convert_from_path
from PIL import Image
import aspose.words as aw
import os, re, pprint

class Creator():
    def __init__(self, folder_root):
        self.root_folder = folder_root
        path = os.path.join(self.root_folder, "../pdfCreator/root")
        if not os.path.exists(path):
            os.mkdir(path)
        self.origin_files = path
        self.files_imgs = os.listdir(self.origin_files)

    #Renomeia arquivos de imagens em ordem crescente
    def rename_files(self):
        for page, file in enumerate(self.files_imgs):
            os.rename(f'{self.origin_files}\{file}', f'{self.origin_files}\page_{page + 1}{str(file[-4:])}')
        self.files_imgs = os.listdir(self.origin_files)

    #Extrai imagens das paginas
    def extract_images(self, file_name):
        imgs = convert_from_path(f"{file_name}.pdf", dpi = 200)

        for page, img in enumerate(imgs):
            img.save(f"{self.origin_files}/page_{page+1}.png", "PNG")

    #Rotaciona imagens em 180 Graus
    def rotated_images(self):
        for page, file in enumerate(self.files_imgs):
            origin_img = Image.open(f"{self.origin_files}/page_{page + 1}{str(file[-4:])}")
            rotated_img = origin_img.rotate(180)
            rotated_img.save(f"{self.origin_files}/page_{page+1}.png", "PNG")
            # rotated_img.save(f"{self.origin_files}/page_{page+1}.png", "PNG")
            print(f"img {page} save")

    #Faz a inserção dos arquivos de imagem em uma lista e gera o arquivo de pdf atravéz da mesma
    def create(self, file_name):
        list_img = list()

        for page, file in enumerate(self.files_imgs):
            image = Image.open(rf'{self.origin_files}/page_{page + 1}{str(file[-4:])}')
            if page == 0:
                page_one = image.convert("RGB")
            else:
                new_image = image.convert("RGB")
            list_img.append(image)

        list_img.pop(0)
        page_one.save(rf'{self.root_folder}/{file_name}.pdf', save_all=True, append_images=tuple(list_img))

def laucher():
    pdf = Creator(str(os.getcwd()))
    # pdf.extract_images("file_name")
    # pdf.rotated_images()
    # pdf.rename_files()
    # pdf.create('file_name')

laucher()