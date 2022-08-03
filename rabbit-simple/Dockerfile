FROM rabbitmq
ENV RABBITMQ_USER guest
ENV RABBITMQ_PASSWORD guest
ENV RABBITMQ_PID_FILE /var/lib/rabbitmq/mnesia/rabbitmq
ADD rabbit_simple_up.sh /rabbit_simple_up.sh
RUN chmod +x /rabbit_simple_up.sh
CMD ["/rabbit_simple_up.sh"]