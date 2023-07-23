#include <iostream>
#include <cmath>
#include <functional>
#include <string>

template <class A>
class optional
{
    bool _isValid;
    A _value;

public:
    optional() : _isValid(false) {}
    optional(A value) : _isValid(true), _value(value) {}
    bool isValid() const { return _isValid; }
    A value() const { return _value; }
    std::string toString() const { return _isValid ? "Some(" + std::to_string(_value) + ")" : "None"; }
};

optional<double>
safe_root(double x)
{
    if (x >= 0) return optional<double>{sqrt(x)};
    else return optional<double>{};
};

optional<double> safe_reciprocal(double x)
{
    if (x != 0) return optional<double>{1 / x};
    else return optional<double>{};
};


/*
  Combine two functions that return optional values into one function that returns an optional value.
  In category theory, this is called the Kleisli composition of two functions that return monadic values.
*/

template<class A, class B, class C>
auto kleisli(optional<A> (*f)(A), optional<C> (*g)(B)) {
    return [f, g](double x) -> optional<C>{
        auto temp = f(x);
        if (temp.isValid()) {
            return g(temp.value());
        } else {
            return optional<C>{};
        };
    };
};

int main()
{
    auto combined = kleisli(safe_root, safe_reciprocal);

    std::cout << "combined(4.0) = " << combined(4.0).toString() << std::endl;
    std::cout << "combined(0.0) = " << combined(0.0).toString() << std::endl;
    std::cout << "combined(-1) = " << combined(-1).toString() << std::endl;

    /* prints

    combined(4.0) = Some(0.500000)
    combined(0.0) = None
    combined(-1) = None

    */

}