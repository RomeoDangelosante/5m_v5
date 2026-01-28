def add_bookmark(db, user_id, post_id):
    db.execute(
        'INSERT INTO bookmark (user_id, post_id) VALUES (?, ?)',
        (user_id, post_id)
    )
    db.commit()
def remove_bookmark(db, user_id, post_id):
    db.execute(
        'DELETE FROM bookmark WHERE user_id = ? AND post_id = ?',
        (user_id, post_id)
    )
    db.commit()
def get_user_bookmarks(db, user_id):
    query = """
        SELECT p.id, p.title, p.body, p.created, p.author_id, u.username
        FROM bookmark b
        JOIN post p ON b.post_id = p.id
        JOIN user u ON p.author_id = u.id
        WHERE b.user_id = ?
        ORDER BY b.created DESC
    """
    bookmarks = db.execute(query, (user_id,)).fetchall()
    result = []
    for bookmark in bookmarks:
        post_dict = dict(bookmark)
        post_dict['created'] = datetime.fromisoformat(post_dict['created'])
        result.append(post_dict)
    return result
def is_post_bookmarked(db, user_id, post_id):
    bookmark = db.execute(
        'SELECT 1 FROM bookmark WHERE user_id = ? AND post_id = ?',
        (user_id, post_id)
    ).fetchone()
    return bookmark is not None