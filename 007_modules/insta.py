import instaloader
 
# Get instance
loader = instaloader.Instaloader()

data = loader.download_profile("itzz_kaushik_223",profile_pic_only=True)
# print(data)