from celery import shared_task


@shared_task
def run_email_info():
    """
        Celery shared task to run email information processing.

        This function is intended to handle the necessary processing related to
        email information. The actual implementation for the processing logic
        needs to be created as indicated by the TODO comment.

        This function is marked with the @shared_task decorator, making it
        suitable for scheduling and execution within a Celery task queue.

        Note:
            The implementation details should be added to complete this function.
    """

    # TODO create func
    pass


@shared_task
def run_server_info():
    """
    This function, decorated with @shared_task, is a placeholder for a task that will run server information retrieval processes asynchronously.

    Note:
        - This function is intended to be run asynchronously as a Celery shared task.
        - The implementation to fetch and process server information is yet to be created.
    """

    # TODO create func
    pass
