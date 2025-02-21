## Summary

- aviator-service CRUD 기능 연동
- provision_types, provision_controller 리팩토링

## Description

1. provision_types.go
   - 기존 ProvisionSpec부분 필드 추상화
   - 불필요한 Status 필드 제거하고 Phase 필드 추가
2. provision_controller.go
   - ncpService Reconciler 객체에 포함시켜 초기화
   - 기존 Verb를 통해 Action이 수행되던 부분을 Status에 Phase필드 추가해서 동작하도록 변경

## etc

- Resolves: #커밋 번호
- See Also: #커밋 번호
