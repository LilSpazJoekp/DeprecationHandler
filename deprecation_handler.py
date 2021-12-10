"""Provide the DeprecationHandler class."""

from warnings import warn
import inspect
from typing import Optional


class DeprecationHandler:
    """This class provides easy deprecation helper methods."""

    @staticmethod
    def _generate_message(
        item_type,
        item_name,
        new_item_name,
        remove_version,
        parent_name=None,
        parent_type=None,
    ):
        parent_str = (
            f" for the `{parent_name}` {parent_type}"
            if parent_name and parent_type
            else ""
        )
        message = f"The `{item_name}` {item_type}{parent_str} will be "
        message += (
            f"superseded by `{new_item_name}`. " if new_item_name else "removed. "
        )
        message += f"Support for this {item_type} will be removed in "
        message += (
            f"version {remove_version}." if remove_version else "a future version."
        )
        return message

    def __init__(self, package_name):
        self.package_name = package_name

    def _find_stacklevel(self):
        frame = inspect.currentframe()
        stacklevel = 0
        while frame.f_globals["__package__"] and frame.f_globals[
            "__package__"
        ].startswith(f"{self.package_name}."):
            stacklevel += 1
            frame = frame.f_back
        return stacklevel

    def _show_deprecation_message(self, message, stacklevel):
        if stacklevel is None:
            stacklevel = self._find_stacklevel()
        warn(message, DeprecationWarning, stacklevel=stacklevel)

    def deprecate_argument(
        self,
        *,
        argument_name: Optional[str] = None,
        message: Optional[str] = None,
        method_name: Optional[str] = None,
        new_argument_name: Optional[str] = None,
        remove_version: Optional[str] = None,
        stacklevel: Optional[int] = None,
    ):
        """Show a deprecation warning for a deprecated argument.

        :param argument_name: The name of the argument being deprecated. Required if
            ``message`` is ``None``.
        :param message: Manually provide a warning message. If provided, all other
            arguments except ``stacklevel`` will be ignored. If ``None``, a message will
            be automatically generated (default: ``None``).
        :param method_name: The method the argument belongs to. Required if ``message``
            is ``None``.
        :param new_argument_name: The argument the deprecated argument will be replaced
            with.
        :param remove_version: The version the argument will be removed.
        :param stacklevel: This will be passed to :py:func:`warnings.warn`'s
            ``stacklevel`` parameter. If ``None``, the ``stacklevel`` will be guessed
            based on ``__package__`` (default: ``None``).

        """
        self._show_deprecation_message(
            message
            or self._generate_message(
                "argument",
                argument_name,
                new_argument_name,
                remove_version,
                method_name,
                "method",
            ),
            stacklevel,
        )

    def deprecate_attribute(
        self,
        *,
        attribute_name: Optional[str] = None,
        class_name: Optional[str] = None,
        message: Optional[str] = None,
        new_attribute_name: Optional[str] = None,
        remove_version: Optional[str] = None,
        stacklevel: Optional[int] = None,
    ):
        """Show a deprecation warning for a deprecated attribute.

        :param attribute_name: The name of the attribute being deprecated. Required if
            ``message`` is ``None``.
        :param class_name: The class of the object the attribute belongs to. Required if
            ``message`` is ``None``.
        :param message: Manually provide a warning message. If provided, all other
            arguments except ``stacklevel`` will be ignored. If ``None``, a message will
            be automatically generated (default: ``None``).
        :param new_attribute_name: The attribute the deprecated attribute will be
            replaced with.
        :param remove_version: The version the attribute will be removed.
        :param stacklevel: This will be passed to :py:func:`warnings.warn`'s
            ``stacklevel`` parameter. If ``None``, the ``stacklevel`` will be guessed
            based on ``__package__`` (default: ``None``).

        """
        self._show_deprecation_message(
            message
            or self._generate_message(
                "attribute",
                attribute_name,
                new_attribute_name,
                remove_version,
                class_name,
                "class",
            ),
            stacklevel,
        )

    def deprecate_class(
        self,
        *,
        class_name: Optional[str] = None,
        message: Optional[str] = None,
        new_class_name: Optional[str] = None,
        remove_version: Optional[str] = None,
        stacklevel: Optional[int] = None,
    ):
        """Show a deprecation warning for a deprecated class.

        :param class_name: The class being deprecated. Required if ``message`` is
            ``None``.
        :param message: Manually provide a warning message. If provided, all other
            arguments except ``stacklevel`` will be ignored. If ``None``, a message will
            be automatically generated (default: ``None``).
        :param new_class_name: The class the deprecated class will be replaced with.
        :param remove_version: The version the class will be removed.
        :param stacklevel: This will be passed to :py:func:`warnings.warn`'s
            ``stacklevel`` parameter. If ``None``, the ``stacklevel`` will be guessed
            based on ``__package__`` (default: ``None``).

        """
        self._show_deprecation_message(
            message
            or self._generate_message(
                "class", class_name, new_class_name, remove_version
            ),
            stacklevel,
        )

    def deprecate_method(
        self,
        *,
        class_name: Optional[str] = None,
        message: Optional[str] = None,
        method_name: Optional[str] = None,
        new_method_name: Optional[str] = None,
        remove_version: Optional[str] = None,
        stacklevel: Optional[int] = None,
    ):
        """Show a deprecation warning for a deprecated method.

        :param class_name: The class of the object the method belongs to. Required if
            ``message`` is ``None``.
        :param message: Manually provide a warning message. If provided, all other
            arguments except ``stacklevel`` will be ignored. If ``None``, a message will
            be automatically generated (default: ``None``).
        :param method_name: The method being deprecated. Required if ``message`` is
            ``None``.
        :param new_method_name: The method the deprecated method will be replaced with.
        :param remove_version: The version the method will be removed.
        :param stacklevel: This will be passed to :py:func:`warnings.warn`'s
            ``stacklevel`` parameter. If ``None``, the ``stacklevel`` will be guessed
            based on ``__package__`` (default: ``None``).

        """
        self._show_deprecation_message(
            message
            or self._generate_message(
                "method",
                method_name,
                new_method_name,
                remove_version,
                class_name,
                "class",
            ),
            stacklevel,
        )
