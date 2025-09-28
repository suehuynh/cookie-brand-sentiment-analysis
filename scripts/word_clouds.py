generic_word = ["crumbl", "cookie", "cooky", "one", "eat", "insomnia", "levain", "bakery"]
def replace_generic_word(text):
  for word in generic_word:
    text = text.replace(word, "")
  return text
### CRUMBL COOKIES ###
crumbl_text = " ".join(df[df["brand"]=="Crumbl Cookies"]["clean_review"])
# Drop Crumbl brand in the review
crumbl_text = replace_generic_word(crumbl_text)

wc = WordCloud(width=800, height=400, background_color="white").generate(crumbl_text)

plt.figure(figsize=(10,5))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()


### INSOMNIA COOKIES ###
insomnia_text = " ".join(df[df["brand"]=="Insomnia Cookies"]["clean_review"])
# Drop generic word in the review
insomnia_text = replace_generic_word(insomnia_text)

wc = WordCloud(width=800, height=400, background_color="white").generate(insomnia_text)

plt.figure(figsize=(10,5))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()


### LEVAIN BAKERY ###
levain_text = " ".join(df[df["brand"]=="Levain Bakery"]["clean_review"])
# Drop generic word in the review
levain_text = replace_generic_word(levain_text)

wc = WordCloud(width=800, height=400, background_color="white").generate(levain_text)

plt.figure(figsize=(10,5))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
