from app.models.community_pool import CommunityPool
def add_to_pool(db, zone, amount):
    pool = db.query(CommunityPool).filter(CommunityPool.zone == zone).first()

    if not pool:
        pool = CommunityPool(zone=zone, total_funds=0)
        db.add(pool)

    pool.total_funds += amount
    db.commit()
    return pool


def deduct_from_pool(db, zone, amount):
    pool = db.query(CommunityPool).filter(CommunityPool.zone == zone).first()

    if pool and pool.total_funds >= amount:
        pool.total_funds -= amount
        db.commit()
        return True

    return False