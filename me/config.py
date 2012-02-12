
def get_fields():
    return [
        "priv_email",
        "first_name",
        "last_name",
        "font",
        "title",
        "background",
        "website",
        "pub_email"
    ]

def get_field_dict( user, page ):
    fields = {
        "priv_email" : {
            "val" : user.email,
            "txt" : "Private Email"
        },
        "first_name" : {
            "val" : user.first_name,
            "txt" : "First Name"
        },
        "last_name" : {
            "val" : user.last_name,
            "txt" : "Last Name"
        },
        "font" : {
            "val" : page.font,
            "txt" : "Font"
        },
        "title" : {
            "val" : page.title,
            "txt" : "Title"
        },
        "background" : {
            "val" : page.background,
            "txt" : "Background"
        },
        "website"   : {
            "val" : page.website,
            "txt" : "Website"
        },
        "pub_email" : {
            "val" : page.email,
            "txt" : "Public Email"
        }
    }
    return fields
