db.users.find()

db.users.find({}, {new_address: 1, tag: 1})

db.users.find({lang_code_id: 'en'})

db.users.find({lang_code_id: 'en'}).limit(1)

db.users.find({new_address: /Jongno-gu/})

db.users.aggregate([{$group: {_id: '$lang_code_id', count: {$sum: 1}}}])



db.users.insert({new_address: '광화문', tag: '이순신동상'})

db.users.find({new_address: /광화문/})


db.users.update({new_address: '광화문'},{$set: {post_url: '여기로가면되나요?'}})

db.users.remove({new_address: '광화문'})