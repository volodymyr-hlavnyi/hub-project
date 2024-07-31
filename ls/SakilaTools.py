from ls.Actor import Actor
from ls.Film import Film


class SakilaTools:

    @staticmethod
    def get_categories(cursor):
        cursor.execute(
            """
            select 
	            category_id ,
	            name
            from category c
            ;
            """
        )
        result = cursor.fetchall()
        return {key: value for key, value in result}

    @staticmethod
    def get_films_by_category(cursor, category_id, page_number):
        cursor.execute(
            """
            select
                f.film_id,
                f.title,
                f.release_year,
                f.description 
            from film as f
            join
            film_category as fc
            on
            f.film_id = fc.film_id
            where
                fc.category_id = %s
            limit 10
            offset %s
            ;
            """, (category_id, page_number * 10)
        )
        result = cursor.fetchall()
        return [Film(data) for data in result]

    @staticmethod
    def get_actors_by_name(cursor, name):
        cursor.execute(
            """
            SELECT 
            actor_id,
            first_name,
            last_name
            from actor a
            where first_name like %s
            or last_name like %s
            ;
            """, ("%" + name + "%", "%" + name + "%")
        )
        result = cursor.fetchall()
        return [Actor(data) for data in result]

    @staticmethod
    def get_films_by_actor(cursor, actor_id):
        cursor.execute(
            """
                select
        f.film_id,
        f.title,
        f.release_year,
        f.description
        from film as f
        join
        film_actor as a
        on
        f.film_id = a.film_id
        where
        a.actor_id = %s
        limit
        10
         """, (actor_id,)
        )
        result = cursor.fetchall()
        return [Film(data) for data in result]
