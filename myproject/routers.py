class RegionRouter:
    def db_for_read(self, model, **hints):
        region = hints.get('region')
        if region == 'region1':
            return 'region1'
        elif region == 'region2':
            return 'region2'
        elif region == 'region3':
            return 'region3'
        return None

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        db_obj1 = self.db_for_read(obj1.__class__, **hints)
        db_obj2 = self.db_for_read(obj2.__class__, **hints)
        if db_obj1 and db_obj2:
            return db_obj1 == db_obj2
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db in ['region1', 'region2', 'region3']